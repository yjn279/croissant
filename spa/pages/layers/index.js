import React from 'react';

import IconButton from '@mui/material/IconButton';
import SpeedDialIcon from '@mui/material/SpeedDialIcon';

import LayersGet from '@components/layers/get';
import LayersPost from '@components/layers/post';


export default function Layers() {

    const [lastCreated, setLastCreated] = React.useState(null);
    const [open, setOpen] = React.useState(false);

    return (
        <>
            <LayersGet lastCreated={lastCreated} />
            <LayersPost setLastCreated={setLastCreated} open={open} setOpen={setOpen} />
            <IconButton onClick={() => setOpen(true)}>
                <SpeedDialIcon />
            </IconButton>
        </>
    )
}
