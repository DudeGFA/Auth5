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
const port = 4000

const { web5, did } = await Web5.connect();

console.log(did)

function isUndefinedorNull(value) {
	if (value === undefined || value === null) {
		return true
	}
}

function isUndefinedEmptyorNull(value) {
	if (value === undefined || value === null) {
		return true
	}
	if (!value || Object.keys(value).length === 0) {
		return true
	}
}
app.get('/test', async (req, res) => {
  res.status(200).json({ 'message': 'I am alive' });
});
	
app.post('/', async (req, res) => {
    try {
        let data = req.body;

        if (isUndefinedEmptyorNull(data)) {
            res.status(400).json({ error: 'Bad Request - Incomplete or Malformed Data' });
            return; // Stop further execution, since the data is invalid
        }

        const dataKeys = Object.keys(data);

        try {
            // Use Promise.all to parallelize record fetching
            const fetchedData = await Promise.all(dataKeys.map(async (key) => {
                try {
                    const { record } = await web5.dwn.records.read({
                        from: data[key].did,
                        message: {
                            filter: {
                                recordId: data[key].recordId
                            }
                        }
                    });

                    const text = await record.data.text();
                    return { [key]: text };
                } catch (error) {
                    console.error(error);
                    return { [key]: null };
                }
            }));

            const responseData = fetchedData.reduce((acc, current) => ({ ...acc, ...current }), {});
            res.json(responseData);

        } catch (error) {
            console.error(error);
            res.status(500).json({ error: 'Internal Server Error' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
