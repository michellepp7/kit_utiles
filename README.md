# Proyecto con Git LFS

Este repositorio utiliza Git LFS (Large File Storage) para gestionar archivos pesados, como los ficheros `.parquet`.

## Clonar el Repositorio

Para clonar correctamente el repositorio, incluyendo el contenido de los archivos LFS, utiliza el comando estándar de clonación. Git LFS descargará automáticamente los archivos rastreados:

```bash
git clone <URL-del-repositorio>
- uses: actions/checkout@v4
  with:
    lfs: true # Habilita la descarga de archivos LFS
