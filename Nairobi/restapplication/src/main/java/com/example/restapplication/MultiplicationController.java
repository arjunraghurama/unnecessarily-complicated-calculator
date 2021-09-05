package com.example.restapplication;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MultiplicationController {

	// Getting values from URL query
	@PostMapping("/multiply")
	public Integer Multiply(@RequestParam("a") Integer a, @RequestParam("b") Integer b)
	{
		Integer result = a*b;
		
		return result;
		
	}
}
