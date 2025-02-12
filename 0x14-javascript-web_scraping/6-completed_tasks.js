#!/usr/bin/node
const request = require('request');

const Url = process.argv[2];

request(Url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  } catch (err) {
    console.error(err);
  }
});
