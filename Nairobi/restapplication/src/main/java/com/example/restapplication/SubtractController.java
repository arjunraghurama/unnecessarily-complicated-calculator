package com.example.restapplication;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SubtractController {
	
	// Getting values from request body and mapping it to POJO
	@PostMapping("/subtract")
	public Integer subtract(@RequestBody SubtractNumbers nums)
	{
		Integer result = nums.getFirstNumber() - nums.getSecondNumber();
		return result;
	}
}
