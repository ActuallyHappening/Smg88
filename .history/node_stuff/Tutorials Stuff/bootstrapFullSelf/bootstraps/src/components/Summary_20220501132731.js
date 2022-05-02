import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div className="position-sticky text-center bg-secondary text-light p-1">
      <p className="alert alert-info">
        Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders
      </p>
    </div>
  )
}

export default Summary