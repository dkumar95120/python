import sys
def getNumber():
    err=''
    S = input().strip()

    try:
        number = int(S)

    except ValueError:
        err = 'Numbers only please'

    except IOError:
        err = 'An error occurred trying to read the file.'

    except ImportError:
        err = "NO module found"

    except EOFError:
        err = 'EOF found'

    except KeyboardInterrupt:
        err = 'key board inturrupt'

    # catch all exceptions
    except:
        err = 'An error occurred.'

    finally: # Optional
      if bool(err):
          print(err) # Clean up
          return -1
    return number