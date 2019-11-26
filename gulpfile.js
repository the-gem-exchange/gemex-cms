'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass');
const csso = require('gulp-csso');
const autoprefixer = require('gulp-autoprefixer');

gulp.task('sass:main', function () {
	return gulp.src('./gemex-cms/static/scss/styles.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(autoprefixer({ cascade: false })) // add vendor prefixes
		.pipe(csso()) // minify
		.pipe(gulp.dest('./gemex-cms/static/css/'));
});

gulp.task('sass:admin', function () {
	return gulp.src('./gemex-cms/static/scss/admin/admin.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(autoprefixer({ cascade: false })) // add vendor prefixes
		.pipe(csso()) // minify
		.pipe(gulp.dest('./gemex-cms/static/css/'));
});

gulp.task('watch', function () {
	gulp.watch('**/*.scss', gulp.series('sass:main'));
	gulp.watch('**/*.scss', gulp.series('sass:admin'));
});
