window.onload = function() {
  console.log("Hello");

  $.getJSON("before/FINALDICT.json", function(data){
  		createGraphic(data);
 	});
 	
}


function makeModal(i,j){
	
	name = mainarr[i.toString()][j.toString()].name;
	rating = mainarr[i.toString()][j.toString()].rating;
	length = mainarr[i.toString()][j.toString()].length;
	genre = mainarr[i.toString()][j.toString()].genre;
	imdb = mainarr[i.toString()][j.toString()].imdbrating;
	metascore = mainarr[i.toString()][j.toString()].metascore;
	synopsis = mainarr[i.toString()][j.toString()].synopsis;
	director = mainarr[i.toString()][j.toString()].director;
	cast = mainarr[i.toString()][j.toString()].casts;
	gross = mainarr[i.toString()][j.toString()].gross;

	imgName = "img_" + i.toString() + "_" + j.toString() + ".jpg";

	img = "img/" + imgName

	rating = "<span class=\"labels-left\">Rated </span>" + rating;
	length = "<span class=\"labels-left\">Length </span>" + length;
	genre = "<span class=\"labels-left\">Genre </span>" + genre;
	imdb = "<span class=\"labels-left\">imdb </span>" +"<span class=\"star\">&#9734;</span>" + imdb;
	
	if(metascore > 60)
		backcolor = "#61c74f";
	else
		backcolor = "#ffcc33";

	metascore = "<span class=\"labels-left\">Metasocre </span><span class=\"metascore\" style=\"background-color:" + backcolor +" \"> "+ metascore + "</span>";



	synosis = "<span class=\"labels-left\">Synopis </span>" + synopsis;
	director = "<span class=\"labels-left\">Dir: </span>" + director;
	cast = "<span class=\"labels-left\">Cast: </span>" + cast;
	gross = "<span class=\"labels-left\">Gross </span>" + gross;


	name = "<h1 id=\"name\" >" + name + "</h1>" 


	movieDetails =  rating + "<br />" + length + "<br />" + genre + "<br />" + imdb + "<br />" + metascore + "<br />" + synopsis + "<br />" + director + "<br />" + cast + "<br />" + gross + "<br />";

	movieImg = "<div> <img class=\"image\" src=\"" + img +"\" />  </div>";

	movieDetails = movieImg + "<div class=\"movie-details\" >" + movieDetails + "</div>" 

	movieDetails = "<div class=\"movie-full\" >" + movieDetails + "</div";

	$movieInfo = $("p#movie-info");
	$movieInfo.html(name  + movieDetails )
}

function createGraphic(data){
	let colors = ["#d53e4f","#f46d43","#fdae61","#fee088", "#f6faaa", "#e6f598","#abdda4", "#66c2a5","#7ba5c7", "#a17bc7"]
	// let blackshades = ["rgb(24,24,24)","rgb(32,32,32)","rgb(40,40,40)","rgb(48,48,48)","rgb(56,56,56)","rgb(64,64,64)","rgb(72,72,72)","rgb(80,80,80)","rgb(88,88,88)","rgb(96,96,96)"]
	// let whiteshades = ["rgb(232,232,232)","rgb(224,224,224)","rgb(216,216,216)","rgb(208,208,208)","rgb(200,200,200)","rgb(192,192,192)","rgb(184,184,184)","rgb(176,176,176)","rgb(168,168,168)"]

	
	// let colors = ["rgb(111,111,111,0.2)", "rgb(111,111,111,0.3)","rgb(111,111,111,0.4)","rgb(111,111,111,0.5)","rgb(111,111,111,0.5)","rgb(111,111,111,0.6)","rgb(111,111,111,0.7)","rgb(111,111,111,0.8)","rgb(111,111,111,0.9)","rgb(111,111,111,1)",]

	$dataTable = $("table#data-table") //jquery that gets the table with id=data-table

	for(let i = 0; i < 11; i++){
		let cell = "<th class=\"blinking\" >" + (2000 + i) + "</th>";
		for(let j = 1; j <= 10; j++){
			cell = cell + "<td id=\"" + (2000 + i) + "_" + j + "\" >"+ "" +" </td>";
		}
		let row = "<tr>" + cell + "</tr>";
		$dataTable.append(row);
	}

	arr = []
	mainarr = []
	year = 2000
	arr.push(data)
	

	arr.forEach(function(value){
		mainarr = value
	})

	
	for(let i = 2000; i < 2011; i++){
		for(let j = 1; j < 11; j++){
			// console.log(mainarr[i.toString()][j.toString()]);

			let id = i + "_" + j;
			let color = colors[j-1];
			// console.log(id)
			$td = $("td#" + id);
			$td.text(mainarr[i.toString()][j.toString()].name);
			$td.css("background-color",color);

			// bcolor = blackshades[j-1]
			// tcolor = whiteshades[j-1]
			// $td.css("background-color",bcolor);
			// $td.css("color",tcolor);



			$td.on("mouseover", function(event){ 
				imdb = mainarr[i.toString()][j.toString()].imdbrating;

				$(event.target).html("<a href=\"#modal-id\"  id=\"click-modal\" rel=\"modal:open\">Details</a>");
				
				makeModal(i,j);
				
			});

			$td.on("mouseout", function(event){
				setTimeout(() => {
					$(event.target).text(mainarr[i.toString()][j.toString()].name);
				}, 400);		
				// setTimeout( function(){
				// 	$(event.target).text(mainarr[i.toString()][j.toString()].name);
				// }, 1000);			
			});	

		}

	}	
}

