import React from 'react';

import axios from 'axios';

import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';


function post({

    title=null,
    description=null,
    start_date=null,
    start_time=null,
    end_date=null,
    end_time=null
    
}) {

    const data = {
        'title': title,
        'description': description,
        'start_date': start_date,
        'start_time': start_time,
        'end_date': end_date,
        'end_time': end_time
    };

    console.log(data);

    axios.post('http://127.0.0.1:8000/layers/', data)
  
        .then(res => {
            console.log(res);
        })
        
        .catch(err => {
            console.log('err:', err);
        });

}


export default function Layer() {
    const [startDate, setStartDate] = React.useState(null);
    const [startTime, setStartTime] = React.useState(null);
    return (
        <>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
                <DatePicker
                    label='Basic example'
                    value={startDate}
                    onChange={date => setStartDate(date)}
                    renderInput={params => <TextField {...params} />}
                />
                <TimePicker
                    label='Basic example'
                    value={startTime}
                    onChange={time => setStartTime(time)}
                    renderInput={params => <TextField {...params} />}
                />
            </LocalizationProvider>
            <TextField id="title" label="Title" variant="outlined" />
            <TextField id="description" label="Description" variant="outlined" multiline rows="3" />
            <p>start date</p>
            <input type="date" id="start-date"></input>
            <p>start time</p>
            <input type="time" id="start-time"></input>
            <p>end date</p>
            <input type="date" id="end-date"></input>
            <p>end time</p>
            <input type="time" id="end-time"></input>
            <Button variant="contained" onClick={() => post({
                title: document.getElementById('title').value,
                description: document.getElementById('description').value,
                start_date: document.getElementById('start-date').value,
                start_time: document.getElementById('start-time').value,
                end_date: document.getElementById('end-date').value,
                end_time: document.getElementById('end-time').value
            })}>Create</Button>
      </>
    )
}
