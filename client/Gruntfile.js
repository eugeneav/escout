module.exports = function(grunt) {

  grunt.initConfig(
  {
    pkg: grunt.file.readJSON('package.json'),
    jshint: {
      all: ['Gruntfile.js', 'src/gazer.js']
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
      },
      build: {
      	expand: true,
        src: 'src/*.js',
        dest: 'dist',
      },
    }
  });

  // Load plugin which prvides uglify task
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask("default", [/*"jshint",*/"uglify"]);
};
