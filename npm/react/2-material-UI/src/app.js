import React from 'react';

import { makeStyles } from '@material-ui/core/styles';

import ReactDOM from 'react-dom';

// import Button from '@material-ui/core/Button';
import { Button, Card, CardContent, CardActionArea, CardMedia, Typography, Grid, Griditem } from '@material-ui/core';

const useStyles = makeStyles({
   media: {
      height: 0,
      paddingTop: '56.25%' // 16:9
   },
   card: {
      position: 'relative',
   },
   overlay: {
      position: 'absolute',
      top: '20px',
      left: '65px',
      color: 'black',
      backgroundColor: 'white'
   }
});

function App() {
  const classes = useStyles();
  return (
	<>
	    <Button variant="contained" color="primary">
	      Hello React &amp Material UI
	    </Button>
		<Card>
		  <CardActionArea>
		  <CardContent>
		  <CardMedia component="img" alt="material ui" height="40" style={{width: 40}}
			image="https://material-ui.com/static/logo_raw.svg"
			title="Material UI" />
			<Typography gutterBottom variant="h5" component="h2"
				className={classes.overlay}>
				Material UI</Typography>
		  </CardContent>
		  </CardActionArea>
		</Card>
	</>
  );
}

				// style={{position: 'absolute', top: '20px', left: '70px'}}>
ReactDOM.render(<App />, document.querySelector('#app'));
