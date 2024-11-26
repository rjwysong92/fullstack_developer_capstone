/*jshint esversion: 8 */ const mongoose = require('mongoose');

/*jshint esversion: 8 */ const Schema = mongoose.Schema;

/*jshint esversion: 8 */ const dealerships = new Schema({
	id: {
    type: Number,
    required: true,
	},
	city: {
    type: String,
    required: true
  },
  state: {
    type: String,
    required: true
  },
  address: {
    type: String,
    required: true
  },
  zip: {
    type: String,
    required: true
  },
  lat: {
    type: String,
    required: true
  },
  long: {
    type: String,
    required: true
  },
  short_name: {
    type: String,
  },
  full_name: {
    type: String,
    required: true
  }
});

module.exports = mongoose.model('dealerships', dealerships);
