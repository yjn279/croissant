import React from 'react';

import axios from 'axios';

import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';


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
        })
        
        .catch(err => {
            console.log('err:', err);
        });

};


export default function LayersPost() {

    const [startDate, setStartDate] = React.useState(null);
    const [startTime, setStartTime] = React.useState(null);
    const [endDate, setEndDate] = React.useState(null);
    const [endTime, setEndTime] = React.useState(null);

    return (
        <>
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
        </>
    );
}
