"""Script to apply a patch to an existing yaml config.
   Requires yq tool installed on the machine
   https://mikefarah.github.io/yq/
   """

import os
import sys
from distutils.spawn import find_executable

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import utils
import logging
import yaml
import argparse
from deployments.OpenShiftComponent import OpenShiftComponent

OVERWRITE = 'overwrite'
APPEND = 'append'
BASELINE_CONFIG = 'baseline-config'

class YamlPatch:
    """ Class to perform Yaml Patch"""
    def __init__(self):
        """ initialize YamlPatch object"""
        # The following variables are prepared to be used by OpenShiftComponent.retrieve_config_file() method
        self.name = ''
        self.components = []
        self.environment = ''
        self.subdir = ''

        self.patch_config = ''
        self.base_config = None
        self.game = ''
        self.cloud = ''

    def merge_yaml(self):
        """Function to generate merged yaml config based on the specs provided """

        spec_file = OpenShiftComponent.retrieve_config_file(self, self.subdir, self.patch_config)
        if not spec_file:
            logging.info(f'{self.patch_config} file must be provided in the /projects/buildscript/scripts/configuration/{self.subdir} folder')
            return 1

        with open(spec_file) as spec_fp:
            spec = spec_fp.read()
            try:
                spec_yaml = yaml.safe_load(spec)
            except yaml.constructor.ConstructorError:
                logging.error(f"Could not load {spec_file}. Please make sure that patch config file is in a valid yaml format.")
                return 1

        if not isinstance(spec_yaml, dict) or 'baseline-config' not in spec_yaml.keys():
            logging.error(f'{spec_file} must specify a "baseline-config: <file>" directive')
            return 1

        if 'merge-rule' not in spec_yaml.keys():
            logging.error(f'{spec_file} must specify "merge-rule: append|overwrite|merge" directive')
            return 1

        baseline_config = spec_yaml.pop('baseline-config')
        # override baseline_config if user has explicitly provided one
        if self.base_config:
            self.base_config = os.path.join(os.path.dirname(spec_file), self.base_config)

        baseline_file = OpenShiftComponent.retrieve_config_file(self, self.subdir, baseline_config, config_file=self.base_config)

        if baseline_file is None:
            logging.error(f'Unable to find a configuration file for {baseline_config}!')
            return 1

        logging.info(f'Using {baseline_file} as the base configuration')

        merge_rule = spec_yaml.pop('merge-rule')
        # create temp file for the patch-config
        patch_file = f'{baseline_config}-patch'
        with open(patch_file, 'w') as patch_fp:
            yaml.safe_dump(spec_yaml, patch_fp,
                           encoding=('utf-8'), default_flow_style=False, allow_unicode=True)

        if merge_rule == APPEND:
            config, stderr, _ = utils.command(f'yq merge --append {baseline_file} {patch_file}')
        elif merge_rule == OVERWRITE:
            config, stderr, _ = utils.command(f'yq merge --overwrite {baseline_file} {patch_file}')
        else:
            config, stderr, _ = utils.command(f'yq merge {baseline_file} {patch_file}')

        logging.error(stderr)
        os.remove(patch_file)

        with open(f'{self.patch_config}_merged', 'w') as merged_fp:
            merged_fp.write(config)
            logging.info(f'{self.patch_config}_merged file has been created with merged contents')

        return 0

    def main(self):
        """Processes arguments for the tool, preparing things for Run.
        Args:
            args -
            --patch_config file containing instructions for baseline-config and merge-rule along with specs to merge in yaml format
            --subdir Subdirectory under configuration directory for the patch configuration file
            --base_config used as baseline config file instead of one specified in the patch_config file only basename is required
            --game [ody, wiso, niso, miso, sixo, gof] specifies the game to use for computing the baseline config file
            --env specifies the environment [live, staging, qa]
            --cloud [aws,mzc]
            """
        utils.setup_logging()

        if not bool(find_executable('yq')):
            logging.error('Unable to find /tools/bin/yq executable to merge requested yaml file')
            return 1

        parser = argparse.ArgumentParser(description='DSYM file processor and uploader')

        parser.add_argument('-p', '--patch_config', action='store',
                            help='Patch configuration to apply.', required=True)

        parser.add_argument('-s', '--subdir', action='store',
                            help='Subdirectory under script/configuration folder where the file is located.', required=True)

        parser.add_argument('-b', '--base_config', action='store',
                            help='Base configuration to use.', required=False)

        parser.add_argument('-g', '--game', action='store',
                            help='game for which config is generated', required=False)

        parser.add_argument('-e', '--env', action='store',
                            help='Environment for which config is generated', required=False)

        parser.add_argument('-c', '--cloud', action='store',
                            help='Cloud for which config is generated', choices=['aws', 'mzc'], required=False)

        parsed_args = parser.parse_args()

        self.patch_config = parsed_args.patch_config
        self.subdir = parsed_args.subdir
        self.base_config = parsed_args.base_config
        self.game = parsed_args.game
        self.environment = parsed_args.env
        self.cloud = parsed_args.cloud
        if self.cloud:
            self.name = f'{self.cloud}_{self.game}_{self.environment}'
            if self.cloud == 'aws':
                self.components.append('AwsComponent')
        else:
            self.name = f'{self.game}_{self.environment}'

        return self.merge_yaml()

if __name__ == "__main__":
    sys.exit(YamlPatch().main())
