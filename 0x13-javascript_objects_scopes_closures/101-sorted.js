#!/usr/bin/node

// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const data = require('./101-data.js');
const dict = data.dict;

let userId = {}
for (const key in dict) {
	const occur = dict[key];
	if (Array.isArray(occur)) {
		for (const id of occur) {
			if (!userId[id]) {
				userId[id] = [];
			}
			userId[id].push(key);
		}
	}
}

console.log(userId);
