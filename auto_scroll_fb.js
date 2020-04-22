setInterval( () => {
	var lk = document.querySelectorAll('.sx_bbcf2c');
	for (let i = 0; i < lk.length; i++) {
		lk[i].click();
		window.scrollBy(0, 500);
	}
}, 3000);
