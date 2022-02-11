let currentDate = new Date()

$(document).ready(function () {
  document.getElementById('btn').addEventListener('click', () => {
    let id = Number(document.getElementById('btn').value)
    let csrf = document.getElementById('csrf').value
    let book_name = document.getElementById('book_name').value
    let book_email = document.getElementById('book_email').value
    let book_number = document.getElementById('book_number').value
    let year = document.getElementById('year').value
    let month = document.getElementById('month').value
    let day = document.getElementById('day').value
    let from_time = document.getElementById('from_time').value
    let to_time = document.getElementById('to_time').value
    let message = document.getElementById('message').value

    if (year < currentDate.getUTCFullYear()) alert('Enter a valid year')
    else if (month < currentDate.getMonth() + 1) alert('Enter a valid month')
    else if (month >= currentDate.getMonth() + 1) {
    } else if (day < currentDate.getDate()) alert('Enter a valid date')
    else if (from_time <= currentDate.getHours())
      alert('Enter a valid time slot')
    else if (Number(from_time) >= Number(to_time))
      alert('Enter a valid time slot')
    else {
      data = {
        csrfmiddlewaretoken: csrf,
        id: id,
        book_name: book_name,
        book_email: book_email,
        book_number: book_number,
        year: year,
        month: month,
        day: day,
        from_time: from_time,
        to_time: to_time,
        message: message,
      }
      $.ajax({
        url: 'auditorium-book',
        method: 'POST',
        data: data,
        dataType: 'json',
        success: (responce) => {
          if (responce.message == '1') {
            $('#sent-message').show()
          } else if (responce.message == '0') {
            $('#error-message').show()
          }
        },
      })
    }
  })
})
