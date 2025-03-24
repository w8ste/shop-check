use tesseract::Tesseract;

pub fn image_to_text() {
    let text = Tesseract::new(None, Some("deu"))
        .unwrap()
        .set_image("zettel.png")
        .unwrap()
        .get_text()
        .unwrap();

    println!("Recognized text: {}", text);
}
