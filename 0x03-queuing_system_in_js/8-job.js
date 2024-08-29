const createPushNotificationsJobs = (jobs, queue) => {
    if (!(Array.isArray(jobs))) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach(jobData => {
        const job = queue.create('push_notification_code_3', jobData);

        job.save(err => {
            if (err) {
                console.error('Failed to create job:', err);
                return;
            }

            console.log(`Notification job created: ${job.id}`);

            // Set up event handlers after the job has been saved
            job.on('complete', () => {
                console.log(`Notification job ${job.id} completed`);
            });

            job.on('failed', (err) => {
                console.log(`Notification job ${job.id} failed: ${err.message}`);
            });

            job.on('progress', (progress) => {
                console.log(`Notification job ${job.id} ${progress}% complete`);
            });
        });
    });
};

module.exports = createPushNotificationsJobs;
