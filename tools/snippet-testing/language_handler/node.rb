require_relative 'base_handler'

module LanguageHandler
  class Node < BaseHandler
    LANG_CNAME = 'js'.freeze

    def self.run_before_test(directory)
      Dir.chdir(directory) do
        output = `npm run format:js 1>/dev/null && npm run test:js -- --fix`
        if $? != 0
          abort(output)
        end
      end
    end

    private

    def execute_command(file)
      execute_with_suppressed_output(
        "NODE_TLS_REJECT_UNAUTHORIZED=0 NODE_PATH=#{dependencies_directory} node #{file}",
        file
      )
    end


  end
end
