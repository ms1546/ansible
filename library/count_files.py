#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def count_files(directory):
    try:
        return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
    except Exception as e:
        return str(e)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
        )
    )

    path = module.params['path']
    files_count = count_files(path)

    result = {
        "path": path,
        "files_count": files_count
    }

    module.exit_json(changed=False, **result)

if __name__ == '__main__':
    main()
