import TextField from '@mui/material/TextField';


export default function Home() {
    return (
    <>
       <input type="date"></input>
       <input type="date"></input>
       <TextField id="standard-basic" label="Standard" variant="standard" inputProps={{maxlength: 64}} />
       <TextField id="outlined-basic" label="Outlined" variant="outlined" />
       <input type="checkbox"></input>
       <input type="reset"></input>
       <select name="choice">
  <option value="first">First Value</option>
  <option value="second" selected>Second Value</option>
  <option value="third">Third Value</option>
</select>
    
    </>
    );
}