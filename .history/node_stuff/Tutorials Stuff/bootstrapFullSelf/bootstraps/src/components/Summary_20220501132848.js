import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <p className="text-center">
        Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders
    </p>
  )
}

export default Summary