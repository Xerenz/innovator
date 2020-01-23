const nodemailer = require("nodemailer");
const fs = require("fs");

function mail() {
	const data = JSON.parse(fs.readFileSync("failed.json"));

	const body1 = `Hi,

Thank you for registering for Innovators' Summit. This mail is to confirm that the program will be held as scheduled on 25 January. The registration desk opens at 8:00 am and closes at 9:00 am. The venue for the event is Seminar Complex, Cochin University of Science and Technology. The location for the same is given below.
https://goo.gl/maps/mzMkgdhbhsueZZAM9 

This mail is attached with your event ticket. Please show this ticket at the registration desk.

As you have registered for the Track-1 workshop on "Power of Serverless with AWS Amplify", please bring your laptops with the prerequisite - Nodejs, Amplify CLI (installed and configured), AWS account, VS Code (or any other code editor) and Git. 

CloudSploit is giving away 1 month of Standard service to anyone who registers, with bigger coupons available at the event.
CloudSploit is the leading open source cloud security monitoring service. They've been recognized by SANS and received other accolades by startups and big companies around the world.

For the event to go smoothly you are requested to be at the venue on time.

We have special vouchers for early registrations. Hope we'll see on the event day.

For any queries regarding the event please feel free to contact:

Amal - 8593054259
Alan - 8547963714

Cheers!

Innovators' Summit`

	const body2 = `Hi,

Thank you for registering for Innovators' Summit. This mail is to confirm that the program will be held as scheduled on 25 January. The registration desk opens at 8:00 am and closes at 9:00 am. The venue for the event is Seminar Complex, Cochin University of Science and Technology. The location for the same is given below.
https://goo.gl/maps/mzMkgdhbhsueZZAM9 

This mail is attached with your event ticket. Please show this ticket at the registration desk.

CloudSploit is giving away 1 month of Standard service to anyone who registers, with bigger coupons available at the event.
CloudSploit is the leading open source cloud security monitoring service. They've been recognized by SANS and received other accolades by startups and big companies around the world.

For the event to go smoothly you are requested to be at the venue on time.

We have special vouchers for early registrations. Hope we'll see on the event day.

For any queries regarding the event please feel free to contact:

Amal - 8593054259
Alan - 8547963714

Cheers!

Innovators' Summit`

	let failed = []

	data.forEach(function(doc) {
		let smtpTransport = nodemailer.createTransport({
			service : "Gmail",
			auth : {
				user : "innovatorssummit01@gmail.com",
				pass : "Summit@2019"
			}
		});

		if (doc.topic === "Innovator's Summit Ticket - Track-1 - Professional" || doc.topic === "Innovator's Summit Ticket - Track-1 - Student")
			mailBody = body1;
		else mailBody = body2;

		let msg = {
			to : doc.email,
			from : "Innovators' Summit <innovatorssummit01@gmail.com>",
			subject : "Innovators' Summit - Ticket",
			text : mailBody,
			attachments : [
				{
					filename : "Innovators' Summit Ticket.pdf",
					path : "./qr_tickets/" + doc.name + ".pdf"
				}
			]
		};

		smtpTransport.sendMail(msg, function(err) {
			if (err) {
				failed.push(doc);
				fs.writeFileSync("failed.json" ,JSON.stringify(failed));
				return console.log("Failed for", doc.name);
			}
			else console.log("mail sent to", doc.name);
		});

	});
}

mail()