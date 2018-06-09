========
Micropad
========

Pad que utiliza o editor do VSCode, o Microsoft Mônaco.


Funcionalidades esperadas
=========================

* Aceita edição anônima
* Determina o tipo de arquivo pela extensão na URL
  (ex.: foo/bar/my-file.py deve abrir um editor no modo Python)
* Entende estrutura de pastas
  (ex.: foo/bar/ deve mostrar todos arquivos e pastas filhas de foo/bar/. Esta
  localização corresponde a uma pasta e não a um arquivo)


Extras
======

* Aceita usuários logados que podem protejer as URLs que quiserem (exceto se já 
  estiver sido protegida por outro usuário)
* Controle de versão: é possível salvar uma versão estática (não pode ser editada)
  usando o caractere de ~ como em: foo/bar/my-file.py~v1
* Usuário dono de uma página consegue dar permissão de escrita para outros 
  usuários.
* Usuário dono de uma página pode controlar nível de acesso (público, somente 
  para leitura, privado)
* O que a criatividade inventar...
