Dies ist eine Vorlage zu erstellung von Streamlit Components.

Der Names des neuen Component muss über dort wo aktuell "st_ant_carousel" steht geändert werden.

    MANIFEST.in
    setup.py
    st_ant_carousel - Ordner
    st_ant_carousel/fronted/package.json

    st_ant_carousel/frontend/src/AntCarousel.tsx
    st_ant_carousel/fronted/src/index.tsx


node.js muss ebenfall installiert sein. 
Öffne ein neues Terminal und navigiere in den Ordner st_ant_carousel/fronted

    npm install --legacy-peer-deps (immer mit --legacy-peer-deps installieren)
    npm run start  -> Nun läuft der Frontend Server


Build

    im Frontend Ordner:

    npm run build

    im Root Ordner:

    python setup.py bdist_wheel

    Upload zu PyPi:

    twine upload dist/*




