const createPushNotificationsJobs = (jobs, queue) => {
    if (!(Array.isArray(jobs))) {
        throw new Error('Jobs is not an array')
    }
    jobs.forEach(j => {
        const job = queue.create('push_notification_code_3', j)
        .save(err => {
            if (!err) console.log(`Notification job created: ${job.id}`)
        })
        .on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        })
        .on('failed', (err) => {
            console.log(`Notification job JOB_ID failed: ${err.message}`)
        })
        .on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`)
        })
    })
}

module.exports = createPushNotificationsJobs