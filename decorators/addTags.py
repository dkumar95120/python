def AddTags(*tags):
    def decorator(oldFunc):
        def inside(*args, **kwargs):
            code = oldFunc(*args, **kwargs)
            for tag in reversed(tags):
                code = f"<{tag}>{code}</{tag}>"
            return code
        return inside
    return decorator

@AddTags("p","i","b")
def MyWebWelcome(name):
    return f"Welcome {name} to my blog!"

print(MyWebWelcome("Kumar"))

