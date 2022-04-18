import React from 'react';

import axios from 'axios';

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';

import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';


const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: '75%',
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};


export default function LayersPost({setLastCreated, open, setOpen}) {

    const [startDate, setStartDate] = React.useState(null);
    const [startTime, setStartTime] = React.useState(null);
    const [endDate, setEndDate] = React.useState(null);
    const [endTime, setEndTime] = React.useState(null);

    const create = () => {

        const data = {
            'title': document.getElementById('title').value,
            'description': document.getElementById('description').value,
            // 'parent': document.getElementById('parent').value,
            // 'start_date': document.getElementById('start-date').value,
            // 'start_time': document.getElementById('start-time').value,
            // 'end_date': document.getElementById('end-date').value,
            // 'end_time': document.getElementById('end-time').value
        };
    
        axios.post('http://127.0.0.1:8000/layers/', data)
      
            .then(res => {
                console.log(res);
                setLastCreated(res.data.id);
                setOpen(false);
            })
            
            .catch(err => {
                console.log('err:', err);
            });
    
    };

    return (
        <Modal
            open={open}
            onClose={() => setOpen(false)}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box sx={style}>
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                    <DatePicker
                        id="start-date"
                        label='Basic example'
                        value={startDate}
                        onChange={date => setStartDate(date)}
                        renderInput={params => <TextField {...params} />}
                    />
                    <TimePicker
                        id="start-time"
                        label='Basic example'
                        value={startTime}
                        onChange={time => setStartTime(time)}
                        renderInput={params => <TextField {...params} />}
                    />
                    <DatePicker
                        id="end-date"
                        label='Basic example'
                        value={endDate}
                        onChange={date => setEndDate(date)}
                        renderInput={params => <TextField {...params} />}
                    />
                    <TimePicker
                        id="end-time"
                        label='Basic example'
                        value={endTime}
                        onChange={time => setEndTime(time)}
                        renderInput={params => <TextField {...params} />}
                    />
                </LocalizationProvider>

                <TextField id="title" label="Standard" variant="standard" inputProps={{maxlength: 64}} />
                <TextField id="description" label="Outlined" variant="outlined" />
                <input type="checkbox"></input>
                <input type="reset" onClick={create}></input>
                <select name="choice" id="parent">
                    <option value="first">First Value</option>
                    <option value="second" selected>Second Value</option>
                    <option value="third">Third Value</option>
                </select>
            </Box>
        </Modal>
    );
}
