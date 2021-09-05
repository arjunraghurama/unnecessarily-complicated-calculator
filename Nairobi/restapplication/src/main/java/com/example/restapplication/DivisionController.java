package com.example.restapplication;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DivisionController {

	// Getting value from URL
	@PostMapping("/division/{a}/{b}")
	public Integer Division(@PathVariable Integer a , @PathVariable Integer b)
	{
		Integer result  = a/b;
		return result;
	}
}
