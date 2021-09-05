package com.example.restapplication;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ParseAndComputeController {

	@PostMapping("/parse")
	public ResponseEntity<Integer> asd()
	{
		return new ResponseEntity<Integer>( 0 , HttpStatus.OK );
	}
}
