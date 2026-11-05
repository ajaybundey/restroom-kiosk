# Restroom Kiosk

A restroom pass kiosk in one offline web page, for any school's bell schedule. Students type their ID to sign out, get in line, or sign back in. The pass shows who is out and for how long.

![Restroom kiosk](docs/restroom-kiosk.png)

(All names above are made up.)

## Using it

Double-click `Restroom_Kiosk.html` to open it in a browser. It needs no install and no internet connection.

| File | What it is |
|---|---|
| `Restroom_Kiosk.html` | The kiosk |
| `teacher-guide.docx` | Teacher guide: setup, step by step, and everyday use (Word) |
| `setup-video.mp4` | Teacher setup video, about 3 minutes |
| `student-guide.pdf` | One-page student guide, to print and post by the kiosk |
| `student-video.mp4` | Student video, about 1 minute |

## Bell schedule

Nothing is built in. In Teacher view, open **Schedule**, then go to **Weekly schedules and special dates**. Type one day's periods and start and end times, or upload a CSV with Period, Start and End columns. Click **Save schedule**. Then click **Copy and save** with **Monday to Friday** selected. Any day that's different, such as an early-release Wednesday, or a single date like a testing day, can be edited on its own.

## Student data

Sign-out logs are stored in the browser on that computer. Backups and exports contain student names and IDs: keep them off shared drives and never commit them. `.gitignore` blocks `.json`, `.csv` and Excel files.

## License

MIT. See [LICENSE](LICENSE).
