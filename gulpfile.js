'use strict';

const gulp  = require('gulp');
const sass  = require('gulp-sass');
const csso  = require('gulp-csso');

gulp.task('sass:main', function () {
	return gulp.src('./gemex-cms/static/scss/styles.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(csso()) // Minify CSS
		.pipe(gulp.dest('./gemex-cms/static/css/'));
});

gulp.task('watch', function () {
	gulp.watch('**/*.scss', gulp.series('sass:main'));
});
