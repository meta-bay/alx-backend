#!/usr/bin/node
/**
 * Writing the test for job creation
 */
import { createQueue } from 'kue';
import chai from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

const { expect } = chai;

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    sinon.restore();
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(1, queue)).to.throw('Jobs is not an array');
  });

  it('should throw if queue is not a valid kue', () => {
    expect(() => createPushNotificationsJobs(jobs, '')).to.throw();
  });

  it('should create jobs correctly', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(console.log.calledOnceWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.true;
  });

  it('should handle job progress event report', (done) => {
    createPushNotificationsJobs(jobs, queue);
    const job = queue.testMode.jobs[0];

    job.on('progress', (progress) => {
      const id = job.id;
      expect(console.log.calledWith(`Notification job ${id} ${progress}% complete`)).to.be.true;
      done();
    });

    job.emit('progress', 50, 100);
  });

  it('should handle job failed event report', (done) => {
    createPushNotificationsJobs(jobs, queue);
    const job = queue.testMode.jobs[0];

    job.on('failed', (err) => {
      const id = job.id;
      expect(console.log.calledWith(`Notification job ${id} failed: ${err.message}`)).to.be.true;
      done();
    });

    job.emit('failed', new Error('job failed!'));
  });

  it('should handle job completed event report', (done) => {
    createPushNotificationsJobs(jobs, queue);
    const job = queue.testMode.jobs[0];

    job.on('complete', () => {
      const id = job.id;
      expect(console.log.calledWith(`Notification job ${id} completed`)).to.be.true;
      done();
    });

    job.emit('complete');
  });
});
