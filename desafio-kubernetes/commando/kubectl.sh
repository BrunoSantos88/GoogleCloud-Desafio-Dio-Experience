##########################################################

- kubectl get nodes
- kubectl get svc 
- kubectl get pod
- kubectl get namespaces


###########################################################
acesso ao pod

- kubectl get pod

- Id pod mysql-c799f89d-pdg5m

- /bin/bash  # no final executar acesso

- kubectl exec --tty --stdin mysql-c799f89d-pdg5m /bin/bash