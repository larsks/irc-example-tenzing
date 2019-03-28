from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True, type="str")
        )
    )

    name = module.params["name"]
    module.exit_json(changed=True, name=name)


if __name__ == '__main__':
    main()
