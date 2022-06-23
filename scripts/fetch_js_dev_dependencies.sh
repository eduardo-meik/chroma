cd ..

DIR="dom-2d-camera"
if [ -d "$DIR" ]; then
  echo "dom-2d-camera already exists, skipping: git clone, yarn install, yarn build"
else
    if ! (git clone git@github.com:chroma-core/dom-2d-camera.git) then
        echo "Unable to fetch dom-2d-camera. Are you online?"
    else
        echo "Fetched dom-2d-camera"
        cd dom-2d-camera
        yarn install --frozen-lockfile
        yarn build
        cd ..
    fi
  exit 0
fi

DIR="regl-scatterplot"
if [ -d "$DIR" ]; then
  echo "regl-scatterplot already exists, skipping: git clone, yarn install, yarn build"
else
    if ! (git clone git@github.com:chroma-core/regl-scatterplot.git) then
        echo "Unable to clone regl-scatterplot. Are you online?"
    else
        echo "Fetched regl-scatterplot"
        cd regl-scatterplot
        yarn install --frozen-lockfile
        yarn build
        cd ..
    fi
  exit 0
fi


