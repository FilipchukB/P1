window.onscroll = function showHeder () {

	let heder = document.querySelector('.up');
	if (window.pageYOffset > 200){
		heder.classList.add('h_fixed');
	}	else {
		heder.classList.remove('h_fixed');
	}
}
arrowTop.onclick = function() {
      window.scrollTo(pageXOffset, 0);
    };