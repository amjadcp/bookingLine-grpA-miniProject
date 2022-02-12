let currentDate = new Date()
let currentYear = currentDate.getUTCFullYear()
let currentMonth = currentDate.getMonth() + 1
let currentDay = currentDate.getDate()
let currentTime = currentDate.getHours()
$(document).ready(function () {
  document.getElementById('btn').addEventListener('click', () => {
    $('#sent-message').hide()
    $('#error-message').hide()
    $('#loading').show()
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

    if (
      book_name == '' ||
      book_number == '' ||
      year == '' ||
      month == '' ||
      day == '' ||
      day == '' ||
      from_time == '' ||
      to_time == ''
    ) {
      alert('Fill the form completely')
    }

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

    if (Number(year) < currentYear) alert('Enter a valid year')
    else if (Number(from_time) >= Number(to_time))
      alert('Enter a valid time slot')
    else if (Number(year) == currentYear) {
      if (Number(month) < currentMonth) alert('Enter a valid month')
      else if (Number(month) == currentMonth) {
        if (Number(day) < currentDay) alert('Enter a valid day')
        else {
          $.ajax({
            url: 'auditorium-book',
            method: 'POST',
            data: data,
            dataType: 'json',
            success: (responce) => {
              if (responce.message == '1') {
                $('#loading').hide()
                $('#sent-message').show()
              } else if (responce.message == '0') {
                $('#loading').hide()
                $('#error-message').show()
              }
            },
          })
        }
      } else {
        $.ajax({
          url: 'auditorium-book',
          method: 'POST',
          data: data,
          dataType: 'json',
          success: (responce) => {
            if (responce.message == '1') {
              $('#loading').hide()
              $('#sent-message').show()
            } else if (responce.message == '0') {
              $('#loading').hide()
              $('#error-message').show()
            }
          },
        })
      }
    } else {
      $.ajax({
        url: 'auditorium-book',
        method: 'POST',
        data: data,
        dataType: 'json',
        success: (responce) => {
          if (responce.message == '1') {
            $('#loading').hide()
            $('#sent-message').show()
          } else if (responce.message == '0') {
            $('#loading').hide()
            $('#error-message').show()
          }
        },
      })
    }
    // $('#book_name').html(' ')
    // $('#book_email').html(' ')
    // $('#book_number').html(' ')
    // $('#message').html(' ')
  })
})
