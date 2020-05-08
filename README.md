# Exemplo de extração de entidades de página do Arquivo.pt

## Download 

https://github.com/arquivo/demo-extrair-entidades/archive/master.zip

## Instalar

Instalar python 3 e pip 

https://www.python.org/downloads/

Na pasta onde está este código, correr os seguintes comandos na consola:

```
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

## Executar

```
python extrair_entidades.py [url a pesquisar]
```

Por exemplo, este comando vai extrair entidades da última versão arquivada da página "arquivo.pt":
```
$ python extrair_entidades.py arquivo.pt
Miscellaneous entities, e.g. events, nationalities, products or works of art: 
Arquivo.pt?; Campeonato Europeu de Futebol 2004; Expo '98; Investigação; O Jogo; Sobre   Pesquisa avançada; Twitter Facebook Subscreva RSS; Área de imprensa Código-aberto & APIs Termos; Últimas novidades

Named person or family.: 
Acesso Recolha; Colabore Sugira; Formações Contacto; José Saramago Prémio da Literatura; Luís Figo Figo; Notícia do jornal "; Pesquise

Non-GPE locations, mountain ranges, bodies of water: 
Lisboa

Companies, agencies, institutions, etc.: 
Crie
```

## Contacto

André Mourão

andre.mourao@fccn.pt
