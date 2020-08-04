function loadLatest(){
	document.querySelector("#latest").innerText= speed;
	speed = JSON.parse(speed);
	document.querySelector("#DownloadValue").innerText = Math.round(speed.Download.Value) + " " + speed.Download.Unit;
	document.querySelector("#UploadValue").innerText = Math.round(speed.Upload.Value) + " " + speed.Upload.Unit;
	
	date = new Date(Date.parse(filename.replace(".json","")));
	document.querySelector("#Time").innerText = date.toLocaleString();
}

setTimeout(loadLatest, 100);
