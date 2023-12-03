import express from 'express'

import { Web5 } from '@web5/api';
/*
Needs globalThis.crypto polyfill. 
This is *not* the crypto you're thinking of.
It's the original crypto...CRYPTOGRAPHY.
*/
import { webcrypto } from 'node:crypto';

// @ts-ignore
if (!globalThis.crypto) globalThis.crypto = webcrypto;

// console.log('writeResult', record);

const app = express()
app.use(express.json());
const port = 3000

function isUndefinedorNull(value) {
	if (value === undefined || value === null) {
		return True
	}
}

app.get('/', async (req, res) => {
	try {

		const existingDid = req.query.did;
		const recordId = req.query.recordId

		if (isUndefinedorNull(existingDid) || isUndefinedorNull(recordId))
		{
			res.status(400).json({ error: 'Bad Request - Incomplete or Malformed Data' });
		}
		console.log(existingDid, recordId)
		// Make sure Web5 is properly initialized before using it
		const {web5, did} = await Web5.connect({
			connectedDid: existingDid
		});
		
		// console.log(recordId)
		// Reads the indicated record from the user's DWNs
		let { record } = await web5.dwn.records.read({
			message: {
				filter: {
					recordId: recordId
				}
			}
		});

		// assuming the record has a text payload
		const text = await record.data.text();
		// console.log(record)
		// console.log(text)
		res.send(text)
	} catch (error) {
		console.error(error);
		res.status(500).json({error: 'Internal Server Error'});
	}
})

app.post('/create', async (req, res) => {
	try {
  
	  // Make sure Web5 is properly initialized before using it
	  const { web5, did: newDid } = await Web5.connect();
  
	  // Send the response after the asynchronous operations are complete
	  res.send(newDid);
	} catch (error) {
	  console.error(error);
	  res.status(500).json({error: 'Internal Server Error'});
	}
  });

app.post('/', async (req, res) => {
  try {
    const existingDid = req.query.did;
	// const identityAgent = req.query.agent;
    const uploadedData = req.body.data;
	if (isUndefinedorNull(uploadedData) || isUndefinedorNull(existingDid))
	{
		res.status(400).json({ error: 'Bad Request - Incomplete or Malformed Data' });
	}

    // Make sure Web5 is properly initialized before using it
    const {web5, did} = await Web5.connect({
		connectedDid: existingDid
	});

    const { record } = await web5.dwn.records.create({
      data: uploadedData,
      message: {
        dataFormat: 'text/plain',
      },
    });

	// const recordId = await record._recordid
    // Send the response after the asynchronous operations are complete
    res.send(record);
  } catch (error) {
    console.error(error);
    res.status(500).json({error: 'Internal Server Error'});
  }
});

app.put('/', async (req, res) => {
	try {
	  const existingDid = req.query.did;
	  const recordId = req.query.recordId;
	  const updatedData = req.body.data;
	  if (isUndefinedorNull(updatedData) || isUndefinedorNull(existingDid) || isUndefinedorNull(recordId))
	  {
		  res.status(400).json({ error: 'Bad Request - Incomplete or Malformed Data' });
	  }
  
	  // Make sure Web5 is properly initialized before using it
	  const {web5, did} = await Web5.connect({
		  connectedDid: existingDid
	  });
  
	  let { record } = await web5.dwn.records.read({
		message: {
		  filter: {
			recordId: recordId
		  }
		}
	  });

	  const updateResult = record.update({
		data: updatedData,
	  });
  
	//   const readResult = await record.data.text();
	  // Send the response after the asynchronous operations are complete
	  res.send(updateResult);
	} catch (error) {
	  console.error(error);
	  res.status(500).json({error: 'Internal Server Error'});
	}
  });


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
