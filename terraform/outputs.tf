output "lambda_function_name" {
  value = aws_lambda_function.url_shortener.function_name
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.url_table.name
}

output "lambda_arn" {
  value = aws_lambda_function.url_shortener.arn
}
