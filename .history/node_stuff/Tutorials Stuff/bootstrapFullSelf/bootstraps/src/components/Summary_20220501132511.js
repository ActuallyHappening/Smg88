import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div className="position-sticky text-center bg-primary text-light p-1 m-0">
      <p className="alert alert-info">
        Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders
      </p>
    </div>
  )
}

export default Summary