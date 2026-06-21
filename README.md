# Paquete de integración — 4.5 y 4.6 (Tarea 07)

Este paquete contiene los archivos que faltan en tu fork `m0loc89/outline` para
que el pipeline de CI y el análisis de SonarQube corran de verdad.

## Qué contiene

```
.github/workflows/quality.yml      <- pipeline de CI
sonar-project.properties           <- configuración de SonarQube
proyecto_pruebas_e2e/              <- proyecto de pruebas Selenium (4.3)
```

## Cómo integrarlo a tu fork

1. Copia estas carpetas/archivos a la raíz de tu repo local `outline/`
   (el mismo que ya tienes clonado, donde corriste `git remote -v` y viste
   `m0loc89/outline`).

2. Verifica que no pisaste nada importante:
   ```bash
   git status
   ```

3. Agrega y sube los cambios:
   ```bash
   git add .github/workflows/quality.yml sonar-project.properties proyecto_pruebas_e2e/
   git commit -m "Agrega pipeline de CI, configuracion de SonarQube y suite Selenium (Tarea 07)"
   git push origin main
   ```

4. Antes de que el workflow funcione completo, configura los secrets en
   GitHub: **Settings → Secrets and variables → Actions → New repository secret**
   - `SONAR_TOKEN`
   - `SONAR_HOST_URL` (si usas SonarCloud: `https://sonarcloud.io`)

5. Ve a la pestaña **Actions** del repo para ver la ejecución y tomar la
   captura real que pide la sección 4.5.

## Importante: los tests tienen TODOs pendientes

`tests/test_login.py` y `tests/test_document.py` traen pruebas marcadas con
`assert True` y comentarios `# TODO`. Esto es honesto: en tu documento
(`tarea6/main.tex`) esos mismos casos ya estaban como placeholder. Para que
la suite realmente pruebe algo (y no solo "pase" trivialmente), alguien del
equipo necesita completar la lógica real contra el DOM de Outline antes de
tomar la captura final de `pytest` para el documento.
