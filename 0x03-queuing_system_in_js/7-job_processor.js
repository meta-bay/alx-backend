#!/usr/bin/node
/**
 * Track progress and errors with Kue: Create the Job processor
 */
import { createQueue } from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  const total = 100;
  function next(progress) {
    if (progress === 0 || progress === (total / 2)) {
      job.progress(progress, total);
      if (progress === (total / 2)) {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      }
    }
    if (blacklist.includes(job.data.phoneNumber)) {
      return done(new Error(`Phone number ${job.data.phoneNumber} is blacklisted`));
    }
    if (progress === total) {
      return done();
    }
    return next(progress + 1);
  }
  next(0);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
