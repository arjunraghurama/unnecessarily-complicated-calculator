package com.example.restapplication;

import java.util.Map;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AddController {

	// Getting values from request body 
	@PostMapping("/add")
	public Integer Add(@RequestBody Map<String, Integer> json)
	{
		Integer a = json.get("a");
		Integer b = json.get("b");
		return a+b;
	}
}
