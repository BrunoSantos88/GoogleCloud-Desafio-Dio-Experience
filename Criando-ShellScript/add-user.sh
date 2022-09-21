#!/bin/bash
echo "Criando usuários do sistema...."
useradd bruno10 -c "Usuário convidado" -s /bin/bash -m -p $(openssl passwd -crypt Senha123) -G GRP_ADM
passwd bruno10 -e
useradd bruno15 -c "Usuário convidado" -s /bin/bash -m -p $(openssl passwd -crypt Senha123) -G GRP_VEN
passwd bruno15 -e
useradd bruno20 -c "Usuário convidado" -s /bin/bash -m -p $(openssl passwd -crypt Senha123) -G GRP_ADM
passwd bruno20 -e
useradd bruno30 -c "Usuário convidado" -s /bin/bash -m -p $(openssl passwd -crypt Senha123) -G GRP_SEC
passwd bruno30 -e
echo "Finalizado!!"
