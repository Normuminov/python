import json, platform

# Collect the data about the system
info = {
    "architecture": platform.architecture(),
    "java version": platform.java_ver(),
    "c standard library version": platform.libc_ver(),
    "machine": platform.machine(),
    "mac version": platform.mac_ver(),
    "node": platform.node(),
    "platform": platform.platform(),
    "processor": platform.processor(),
    "release": platform.release(),
    "system": platform.system(),
    "uname": platform.uname(),
    "version": platform.version(),
    "windows": {
        "edition": platform.win32_edition(),
        "version": platform.win32_ver(),
        "is iot": platform.win32_is_iot()
    },
    "python": {
        "branch": platform.python_branch(),
        "build": platform.python_build(),
        "compiler": platform.python_compiler(),
        "implementation": platform.python_implementation(),
        "revision": platform.python_revision(),
        "version": platform.python_version()
    }
}

# convert to json format
system_info = json.dumps(info, indent=4)

# output the data
print(system_info)

# create a file system_info.json
file = open("system_info.json", "w+")

# save the date to the file
file.write(system_info)

# close the file
file.close()