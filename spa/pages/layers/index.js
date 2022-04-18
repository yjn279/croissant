import React from 'react';

import LayersGet from '@components/layers/get';
import LayersPost from '@components/layers/post';


export default function Layers() {

    const [lastCreated, setLastCreated] = React.useState(null);

    return (
        <>
            {/* <LayersGet lastCreated={lastCreated} /> */}
            <LayersPost setLastCreated={setLastCreated} />
        </>
    )
}
