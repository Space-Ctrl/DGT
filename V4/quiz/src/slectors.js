
const categories = [ "General Knowledge","Books","Film","Music","Musicals & Theatres","Television","Video Games","Board Games","Science & Nature","Computers","Mathematics","Mythology","Sports","Geography","History","Politics","Art","Celebrities","Animals", "Vehicles","Comics","Gadgets", "Japanese Anime & Manga","Cartoon & Animations"];
  
 function createCategoryOptions() {
    const categorySelect = document.getElementById("catagories");
    for (let i = 0; i < categories.length; i++) {
      const option = document.createElement("option");
      option.text = categories[i];
      categorySelect.appendChild(option);
    }
  }

  function handleCategorySelect(event) {
    const selectedValue = event.target.value;
    console.log(`Selected category: ${selectedValue}`);
  }

  const categorySelect = document.getElementById("catagories");
  categorySelect.addEventListener("change", handleCategorySelect);

  // Call the function to generate the options
  createCategoryOptions();
