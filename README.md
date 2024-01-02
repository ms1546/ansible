## Requirement
- Ansible

## Usage
- git clone (dist:`/ansible/new_repo/`)
```
ansible-playbook -i inventory.ini playbooks/clone_repo.yml
```
- create `test.txt` (dist:`/ansible/`) and count files (in only `/ansible`)
```
ansible-playbook -i inventory.ini playbooks/count_files.yml
```