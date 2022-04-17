import React from 'react';
import axios from 'axios';
import LayersGet from '../../components/layers/get';
import LayersPost from '../../components/layers/post';
import TextField from '@mui/material/TextField';


function get(setLayers) {

    let test = null;

    axios.get('http://127.0.0.1:8000/layers/')
  
        .then(res => {
            console.log(res);
            test = res.data;
        })
        
        .catch(err => {
           console.log(err);
        });

    return test;

};


const create = () => {

    const data = {
        'title': document.getElementById('title').value,
        'description': document.getElementById('description').value,
        'parent': document.getElementById('parent').value,
        'start_date': document.getElementById('start-date').value,
        'start_time': document.getElementById('start-time').value,
        'end_date': document.getElementById('end-date').value,
        'end_time': document.getElementById('end-time').value
    };

    axios.post('http://127.0.0.1:8000/layers/', data)
  
        .then(res => {
            console.log(res);
        })
        
        .catch(err => {
            console.log('err:', err);
        });

};


export default function Layers() {
    get();
    return (
        <>
            <LayersGet />
            <LayersPost />
        </>
    )
}


// export async function getServerSideProps() {
//     const res = await fetch(`https://.../data`)
//     const data = await res.json()
  
//     // Pass data to the page via props
//     return { props: { data } }
//   }
