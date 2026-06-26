pub fn hide_payload(image_path: &str, payload: &[u8], output_path: &str) -> Result<(), String> {
    todo!()
}

pub fn extract_payload(image_path: &str) -> Vec<u8> {
    todo!()
}

use image::{GenericImageView, GenericImage, Pixel};

pub fn hide_payload(image_path: &str, payload: &[u8], output_path: &str) -> Result<(), String> {
    let mut img = image::open(image_path).map_err(|e| e.to_string())?;
    let (width, height) = img.dimensions();

    let mut bits = Vec::new();
    let len_bytes = (payload.len() as u32).to_be_bytes();
    
    for byte in len_bytes.iter().chain(payload.iter()) {
        for i in (0..8).rev() {
            bits.push((byte >> i) & 1);
        }
    }

    if bits.len() > (width * height * 3) as usize {
        return Err("L'immagine è troppo piccola".to_string());
    }

    let mut bit_iter = bits.iter();

    'outer: for y in 0..height {
        for x in 0..width {
            let pixel = img.get_pixel(x, y);
            let mut rgba = pixel.to_rgba();

            for channel in 0..3 {
                if let Some(&bit) = bit_iter.next() {
                    rgba[channel] = (rgba[channel] & 0xFE) | bit;
                } else {
                    img.put_pixel(x, y, rgba);
                    break 'outer;
                }
            }
            img.put_pixel(x, y, rgba);
        }
    }

    img.save(output_path).map_err(|e| e.to_string())?;
    Ok(())
}

pub fn extract_payload(image_path: &str) -> Result<Vec<u8>, String> {
    let img = image::open(image_path).map_err(|e| e.to_string())?;
    let (width, height) = img.dimensions();

    let mut bits = Vec::new();

    for y in 0..height {
        for x in 0..width {
            let rgba = img.get_pixel(x, y).to_rgba();
            for channel in 0..3 {
                bits.push(rgba[channel] & 1);
            }
        }
    }

    let bits_to_byte = |bit_slice: &[u8]| {
        let mut byte = 0u8;
        for (i, &bit) in bit_slice.iter().enumerate() {
            byte |= bit << (7 - i);
        }
        byte
    };

    if bits.len() < 32 {
        return Err("Immagine corrotta o troppo piccola".to_string());
    }
    
    let mut len_bytes = [0u8; 4];
    for i in 0..4 {
        let start = i * 8;
        len_bytes[i] = bits_to_byte(&bits[start..start + 8]);
    }
    let payload_len = u32::from_be_bytes(len_bytes) as usize;

    if 32 + (payload_len * 8) > bits.len() {
        return Err("Nessun messaggio nascosto valido trovato in questa immagine.".to_string());
    }

    let mut payload = Vec::with_capacity(payload_len);
    for i in 0..payload_len {
        let start = 32 + (i * 8);
        payload.push(bits_to_byte(&bits[start..start + 8]));
    }

    Ok(payload)
}